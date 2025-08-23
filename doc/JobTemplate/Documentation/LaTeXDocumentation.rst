.. _JOBTMPL/LatexDocumentation:

LatexDocumentation
##################

The ``LatexDocumentation`` job template ................

.. topic:: Features

   * Translate a LaTeX document to PDF.

.. topic:: Behavior:

   .. todo:: LatexDocumentation:Behavior needs documentation.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-LatexDocumentation.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * :gh:`addnab/docker-run-action`

     * :dockerhub:`pytooling/miktex:sphinx`


.. _JOBTMPL/LatexDocumentation/Instantiation:

Instantiation
*************

The following instantiation example creates a job `Params` derived from job template `Parameters` version `r0`. It only
requires a `name` parameter to create the artifact names.

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


.. seealso::

   :ref:`JOBTMPL/TagReleaseCommit`
     ``LatexDocumentation`` is usualy

.. _JOBTMPL/LatexDocumentation/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/LatexDocumentation/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/LatexDocumentation/Input/ubuntu_image_version`        | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/LatexDocumentation/Input/document`                    | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/LatexDocumentation/Input/latex_artifact`              | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/LatexDocumentation/Input/pdf_artifact`                | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/LatexDocumentation/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/LatexDocumentation/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/LatexDocumentation/Inputs:

Input Parameters
****************

.. _JOBTMPL/LatexDocumentation/Input/ubuntu_image_version:

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

.. _JOBTMPL/LatexDocumentation/Input/document:

document
========

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/LatexDocumentation/Input/latex_artifact:

latex_artifact
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/LatexDocumentation/Input/pdf_artifact:

pdf_artifact
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/LatexDocumentation/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/LatexDocumentation/Outputs:

Outputs
*******

This job template has no output parameters.

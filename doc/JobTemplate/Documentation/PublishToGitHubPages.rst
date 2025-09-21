.. _JOBTMPL/PublishToGitHubPages:
.. index::
   single: GitHub Pages; PublishToGitHubPages Template
   single: GitHub Action Reusable Workflow; PublishToGitHubPages Template

PublishToGitHubPages
####################

This job template publishes HTML content from artifacts of other jobs to GitHub Pages.

.. topic:: Features

   tbd


.. topic:: Behavior

   1. Checkout repository.
   2. Download artifacts.
   3. Push HTML files to branch ``gh-pages``.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-PublishToGitHubPages.png
      :width: 500px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`


.. _JOBTMPL/PublishToGitHubPages/Instantiation:

Instantiation
*************

.. grid:: 2

   .. grid-item::
      :columns: 5

      .. rubric:: Simple Example

      .. code-block:: yaml

         jobs:
           BuildTheDocs:
             # ...

           PublishToGitHubPages:
             uses: pyTooling/Actions/.github/workflows/PublishToGitHubPages.yml@r5
             needs:
               - BuildTheDocs
             with:
               doc: Documentation

   .. grid-item::
      :columns: 5

      .. rubric:: Complex Example

      .. code-block:: yaml

         jobs:
           PublishToGitHubPages:
             uses: pyTooling/Actions/.github/workflows/PublishToGitHubPages.yml@r5
             needs:
               - Params
               - BuildTheDocs
               - Coverage
               - StaticTypeCheck
             with:
               doc:      ${{ fromJson(needs.Params.outputs.artifact_names).documentation_html }}
               coverage: ${{ fromJson(needs.Params.outputs.artifact_names).codecoverage_html }}
               typing:   ${{ fromJson(needs.Params.outputs.artifact_names).statictyping_html }}


.. _JOBTMPL/PublishToGitHubPages/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/PublishToGitHubPages/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/PublishToGitHubPages/Input/ubuntu_image_version`      | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishToGitHubPages/Input/doc`                       | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishToGitHubPages/Input/coverage`                  | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishToGitHubPages/Input/typing`                    | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/PublishToGitHubPages/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/PublishToGitHubPages/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/PublishToGitHubPages/Inputs:

Input Parameters
****************

.. _JOBTMPL/PublishToGitHubPages/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/PublishToGitHubPages/Input/doc:

doc
===

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid artifact name.
:Description:     Name of the documentation artifact containing the HTML website.


.. _JOBTMPL/PublishToGitHubPages/Input/coverage:

coverage
========

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the coverage artifact containing the HTML coverage report, which will be integrated as a
                  subdirectory.


.. _JOBTMPL/PublishToGitHubPages/Input/typing:

typing
======

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the type checking artifact containing the HTML type checker report, which will be integrated
                  as a subdirectory.


.. _JOBTMPL/PublishToGitHubPages/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/PublishToGitHubPages/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/PublishToGitHubPages/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

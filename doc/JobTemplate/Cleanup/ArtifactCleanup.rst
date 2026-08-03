.. _JOBTMPL/ArtifactCleanup:
.. index::
   single: delete-artifact; ArtifactCleanUp Template
   single: GitHub Action Reusable Workflow; ArtifactCleanUp Template

ArtifactCleanUp
###############

.. attention::

   This job template is **deprecated** and will be removed in ``r8``. Use :ref:`JOBTMPL/CleanupArtifacts` instead,
   which resolves artifact names from the ``artifact_names`` JSON dictionary produced by :ref:`JOBTMPL/Parameters`
   and can delete two independently guarded sets of artifacts. The job template emits the same warning at runtime.

This job removes artifacts which were used to exchange data between jobs.

.. topic:: Features

   * Delete artifacts from pipeline.

.. topic:: Behavior

   1. Delete the package artifact if the current pipeline run was not a tagged run
      (:ref:`JOBTMPL/ArtifactCleanup/Input/package`).
   2. Delete all remaining artifacts if given as a parameter
      (:ref:`JOBTMPL/ArtifactCleanup/Input/remaining`).

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-ArtifactCleanup.png
      :width: 350px

.. topic:: Dependencies

   * :gh:`geekyeggo/delete-artifact`

.. _JOBTMPL/ArtifactCleanup/Instantiation:

Instantiation
*************

Simple Example
==============

The simplest variant just uses the artifact name for the package.

.. code-block:: yaml

   jobs:
     ArtifactCleanUp:
       uses: pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml@r7
       with:
         package: Package


Complex Example
===============

.. code-block:: yaml

   jobs:
     ArtifactCleanUp:
       uses: pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml@r7
       needs:
         - Params
         - UnitTesting
         - BuildTheDocs
         - PublishToGitHubPages
         - PublishTestResults
       with:
         package: ${{ fromJson(needs.Params.outputs.artifact_names).package_all }}
         remaining: |
           ${{ fromJson(needs.Params.outputs.artifact_names).unittesting_xml }}-*


.. seealso::

   :ref:`JOBTMPL/CleanupArtifacts`
     The replacement for this template.
   :ref:`JOBTMPL/IntermediateCleanUp`
     ``IntermediateCleanUp`` is used to remove intermediate artifacts like unit test artifacts for each job variant
     after test results have been merged into a single file. Deprecated as well.


.. _JOBTMPL/ArtifactCleanup/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/ArtifactCleanup/Inputs>`

+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                           |
+=====================================================================+==========+==========+===================================================+
| :ref:`JOBTMPL/ArtifactCleanup/Input/ubuntu_image_version`           | no       | string   | ``'26.04'``                                       |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/ArtifactCleanup/Input/package`                        | yes      | string   | — — — —                                           |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/ArtifactCleanup/Input/remaining`                      | no       | string   | ``''``                                            |
+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/ArtifactCleanup/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/ArtifactCleanup/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/ArtifactCleanup/Inputs:

Input Parameters
****************

.. _JOBTMPL/ArtifactCleanup/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/ArtifactCleanup/Input/package:

package
=======

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Multi-line string accepting any valid artifact name per line.
:Description:     Artifacts to be removed on not tagged runs.


.. _JOBTMPL/ArtifactCleanup/Input/remaining:

remaining
=========

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Multi-line string accepting any valid artifact name per line.
:Description:     Artifacts to be removed on every run, one artifact name per line. |br|
                  Names may end in ``*`` to delete all per-matrix-job variants of an artifact.


.. _JOBTMPL/ArtifactCleanup/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/ArtifactCleanup/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/ArtifactCleanup/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

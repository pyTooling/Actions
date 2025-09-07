.. _JOBTMPL/ArtifactCleanup:

ArtifactCleanUp
###############

This job removes artifacts which were used to exchange data from job to job.

.. topic:: Features

   * Delete artifacts from pipeline.

.. topic:: Behavior

   1. Delete the package artifact if the current pipeline run was not a tagged run.
   2. Delete all remaining artifacts if given as a parameter.

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
       uses: pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml@r5
       with:
         package: Package


Complex Example
===============

.. code-block:: yaml

   jobs:
     ArtifactCleanUp:
       uses: pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml@r5
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

   :ref:`JOBTMPL/IntermediateCleanUp`
     ``IntermediateCleanUp`` is used to remove intermediate artifacts like unit test artifacts for each job variant
     after test results have been merged into a single file.


.. _JOBTMPL/ArtifactCleanup/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/ArtifactCleanup/Inputs>`

+---------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                           |
+=====================================================================+==========+==========+===================================================+
| :ref:`JOBTMPL/ArtifactCleanup/Input/ubuntu_image_version`           | no       | string   | ``'24.04'``                                       |
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
:Description:     Versi


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

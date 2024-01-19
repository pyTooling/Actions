.. _JOBTMPL/ArtifactCleanup:

ArtifactCleanUp
###############

This job removes artifacts used to exchange data from job to job.

**Behavior:**

1. Delete the package artifact if the current pipeline run was not a tagged run.
2. Delete all remaining artifacts if given as a parameter.

**Dependencies:**

* :gh:`geekyeggo/delete-artifact`


Instantiation
*************

Simple Example
==============

The simplest variant just uses the artifact name for the package.

.. code-block:: yaml

   jobs:
     ArtifactCleanUp:
       uses: pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml@r0
       with:
         package: Package


Complex Example
===============

.. code-block:: yaml

   jobs:
     ArtifactCleanUp:
       uses: pyTooling/Actions/.github/workflows/ArtifactCleanUp.yml@r0
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


Parameters
**********

package
=======

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| package        | yes      | string   | — — — —  |
+----------------+----------+----------+----------+

Artifacts to be removed on not tagged runs.


remaining
=========

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| remaining      | optional | string   | ``""``   |
+----------------+----------+----------+----------+

Artifacts to be removed unconditionally.


Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.

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
         package: ${{ fromJson(needs.Params.outputs.params).artifacts.package }}
         remaining: |
           ${{ fromJson(needs.Params.outputs.params).artifacts.unittesting }}-ubuntu-3.9
           ${{ fromJson(needs.Params.outputs.params).artifacts.unittesting }}-ubuntu-3.10


Parameters
**********

package
=======

Artifacts to be removed on not tagged runs.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| yes      | string   | — — — —  |
+----------+----------+----------+

remaining
=========

Artifacts to be removed unconditionally.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | ``""``   |
+----------+----------+----------+

Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.

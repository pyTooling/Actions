.. _JOBTMPL/IntermediateCleanUp:
.. index::
   single: delete-artifact; IntermediateCleanUp Template
   single: GitHub Action Reusable Workflow; IntermediateCleanUp Template

IntermediateCleanUp
###################

.. attention::

   This job template is **deprecated** and will be removed in ``r8``. Use :ref:`JOBTMPL/CleanupArtifacts` instead,
   which covers the intermediate cleanup as well as the final cleanup. :ref:`JOBTMPL/CompletePipeline` already
   instantiates ``CleanupArtifacts.yml`` for both of its cleanup jobs.

   The job template emits the same warning at runtime.

   Migration: the two prefix parameters become entries of
   :ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids` using the postfix form, so the artifact names no longer
   need to be assembled by the caller.

   .. code-block:: yaml

      # before
      sqlite_coverage_artifacts_prefix: ${{ fromJson(needs.Params.outputs.artifact_names).codecoverage_sqlite }}-
      xml_unittest_artifacts_prefix:    ${{ fromJson(needs.Params.outputs.artifact_names).unittesting_xml }}-

      # after
      json: ${{ needs.Params.outputs.artifact_names }}
      artifact-json-ids: >-
        codecoverage_sqlite:-*
        unittesting_xml:-*

The ``IntermediateCleanUp`` job template is used to remove intermediate artifacts like unit test artifacts for each job
variant after test results have been merged into a single file.

.. topic:: Features

   * Delete artifacts from pipeline.

.. topic:: Behavior

   1. Delete all SQLite code coverage artifacts, if a prefix was given
      (:ref:`JOBTMPL/IntermediateCleanUp/Input/sqlite_coverage_artifacts_prefix`).
   2. Delete all JUnit XML report artifacts, if a prefix was given
      (:ref:`JOBTMPL/IntermediateCleanUp/Input/xml_unittest_artifacts_prefix`).

   The job removes the per-matrix-job artifacts once they have been merged, so they don't count against the
   repository's artifact storage for the retention period.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-IntermediateCleanUp.png
      :width: 400px

.. topic:: Dependencies

   * :gh:`geekyeggo/delete-artifact`

.. _JOBTMPL/IntermediateCleanUp/Instantiation:

Instantiation
*************

The following instantiation example creates a ``Params`` job derived from job template ``Parameters`` version ``@r7``. It only
requires a `name` parameter to create the artifact names.

.. code-block:: yaml

   jobs:
     IntermediateCleanUp:
       uses: pyTooling/Actions/.github/workflows/IntermediateCleanUp.yml@r7
       needs:
         - UnitTestingParams
         - PublishCoverageResults
         - PublishTestResults
       if: success() || failure()
       with:
         sqlite_coverage_artifacts_prefix: ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).codecoverage_sqlite }}-
         xml_unittest_artifacts_prefix:    ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).unittesting_xml }}-

.. seealso::

   :ref:`JOBTMPL/CleanupArtifacts`
     The replacement for this template.
   :ref:`JOBTMPL/ArtifactCleanup`
     ``ArtifactCleanup`` is used to remove artifacts like unit test report artifacts after artifact's content has been
     (post-)processed or published. Deprecated as well.


.. _JOBTMPL/IntermediateCleanUp/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/IntermediateCleanUp/Inputs>`

+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| Parameter Name                                                             | Required | Type     | Default                                           |
+============================================================================+==========+==========+===================================================+
| :ref:`JOBTMPL/IntermediateCleanUp/Input/ubuntu_image_version`              | no       | string   | ``'26.04'``                                       |
+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/IntermediateCleanUp/Input/sqlite_coverage_artifacts_prefix`  | no       | string   | ``''``                                            |
+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+
| :ref:`JOBTMPL/IntermediateCleanUp/Input/xml_unittest_artifacts_prefix`     | no       | string   | ``''``                                            |
+----------------------------------------------------------------------------+----------+----------+---------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/IntermediateCleanUp/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/IntermediateCleanUp/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/IntermediateCleanUp/Inputs:

Input Parameters
****************

.. _JOBTMPL/IntermediateCleanUp/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/IntermediateCleanUp/Input/sqlite_coverage_artifacts_prefix:

sqlite_coverage_artifacts_prefix
================================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name including ``*``.
:Description:     Prefix for SQLite coverage artifacts to be removed.


.. _JOBTMPL/IntermediateCleanUp/Input/xml_unittest_artifacts_prefix:

xml_unittest_artifacts_prefix
=============================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name including ``*``.
:Description:     Prefix for XML unittest artifacts to be removed.


.. _JOBTMPL/IntermediateCleanUp/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/IntermediateCleanUp/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/IntermediateCleanUp/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

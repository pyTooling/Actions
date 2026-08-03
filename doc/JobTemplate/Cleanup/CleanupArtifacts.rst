.. _JOBTMPL/CleanupArtifacts:
.. index::
   single: delete-artifact; CleanupArtifacts Template
   single: GitHub Action Reusable Workflow; CleanupArtifacts Template

CleanupArtifacts
################

The ``CleanupArtifacts`` job template deletes pipeline artifacts that were only needed to hand data from one job to
the next.

Artifacts are not addressed by their literal names, but by *keys* into the JSON dictionary of artifact names produced
by :ref:`JOBTMPL/Parameters`. A pipeline therefore never repeats an artifact name, and renaming an artifact in one
place does not silently leave a stale one behind.

Two independent sets of artifacts can be deleted, each guarded by its own condition. That is how
:ref:`JOBTMPL/CompletePipeline` deletes the intermediate reports on every run, but the package artifact only when it
is *not* a release run - on a release run :ref:`JOBTMPL/PublishOnPyPI` consumes and deletes it.

.. note::

   ``CleanupArtifacts`` replaces the deprecated :ref:`JOBTMPL/ArtifactCleanup` and :ref:`JOBTMPL/IntermediateCleanUp`
   templates.

.. topic:: Features

   * Delete artifacts by key into an artifact-name dictionary instead of by literal name.
   * Expand a key to a name with prefix and/or postfix, so the per-matrix-job artifacts of one key can be deleted with
     a single entry.
   * Delete two independent sets of artifacts, each with its own condition.
   * Delete further artifacts by literal name if needed.

.. topic:: Behavior

   1. Compute the names of the first artifact set from :ref:`JOBTMPL/CleanupArtifacts/Input/json` and
      :ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids`.
   2. Delete the computed artifacts, if :ref:`JOBTMPL/CleanupArtifacts/Input/condition` is true.
   3. Compute the names of the second artifact set from :ref:`JOBTMPL/CleanupArtifacts/Input/json2` and
      :ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids2`.
   4. Delete the computed artifacts, if :ref:`JOBTMPL/CleanupArtifacts/Input/condition2` is true.
   5. Delete the artifacts named literally by :ref:`JOBTMPL/CleanupArtifacts/Input/others`.

   .. note::

      Deletions use ``continue-on-error``, so an artifact that does not exist - because the producing job was skipped -
      does not fail the pipeline.

.. topic:: Dependencies

   * :gh:`geekyeggo/delete-artifact`


.. _JOBTMPL/CleanupArtifacts/ArtifactIDs:

Artifact ID Syntax
******************

:ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids` takes a space or newline separated list of entries. Each
entry is resolved against the JSON dictionary given by ``json``. The list of entries in
:ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids2` is looked up in ``json2``:

+------------------------+-----------------------------------------------+
| Entry                  | Resolves to                                   |
+========================+===============================================+
| ``key``                | the artifact name stored under ``key``        |
+------------------------+-----------------------------------------------+
| ``key:postfix``        | the artifact name followed by ``postfix``     |
+------------------------+-----------------------------------------------+
| ``prefix:key``         | ``prefix`` followed by the artifact name      |
+------------------------+-----------------------------------------------+
| ``prefix:key:postfix`` | ``prefix``, the artifact name and ``postfix`` |
+------------------------+-----------------------------------------------+
| ``#key``               | ignored - used to comment out an entry        |
+------------------------+-----------------------------------------------+

.. hint::

   Assume a matrix creating multiple artifacts sharing the same prefix. That prefix is taken from the JSON dictionary,
   e.g. ``artifactNames['unittesting_xml']`` (= ``'myProject-UnitTestReportSummary-XML'``). Each matrix job then adds a
   postfix specific to its matrix combination like operating system, platform details or Python version (=
   ``'-ubuntu-3.14'``). |br|
   The resulting artifact name is ``myProject-UnitTestReportSummary-XML-ubuntu-3.14``.

   To delete all these variants, ``unittesting_xml:-*`` can be used. |br|
   The merged unit test XML artifact is not deleted by this entry, because that one uses
   ``artifactNames['unittesting_xml']`` directly, without a postfix. Deleting it too needs a second entry
   ``unittesting_xml`` - which is why both forms appear in the example below.

.. code-block:: yaml

   artifact-json-ids: >-
     unittesting_xml:-*
     unittesting_xml
     statictyping_html
     #documentation_latex

A key that is not present in the dictionary is reported and skipped.


.. _JOBTMPL/CleanupArtifacts/Instantiation:

Instantiation
*************

The following instantiation example creates an ``ArtifactCleanUp`` job derived from job template
``CleanupArtifacts`` version ``@r7``. It deletes the report artifacts on every run, and the package artifact only when
the pipeline is not a tagged release.

.. code-block:: yaml

   jobs:
     ArtifactCleanUp:
       uses: pyTooling/Actions/.github/workflows/CleanupArtifacts.yml@r7
       needs:
         - Prepare
         - Params
         - UnitTesting
         - Documentation
       if: ${{ !cancelled() }}
       with:
         json: ${{ needs.Params.outputs.artifact_names }}
         artifact-json-ids: >-
           unittesting_xml:-*
           codecoverage_sqlite:-*
           unittesting_xml
           codecoverage_html
           documentation_html
         json2:      ${{ needs.Params.outputs.artifact_names }}
         condition2: ${{ needs.Prepare.outputs.is_release_tag != 'true' }}
         artifact-json-ids2: >-
           package_all

.. attention::

   The job should be given an ``if:`` expression containing a status check function, such as ``!cancelled()``. If no
   such function is present, the cleanup is skipped as soon as a single upstream job was skipped, and the artifacts
   are kept until their retention period expires.


.. seealso::

   :ref:`JOBTMPL/IntermediateCleanUp`
     Deprecated. Deleted the per-matrix-job artifacts in the middle of a pipeline; this template does the same job
     with a ``json`` dictionary instead of two hard-coded prefixes.
   :ref:`JOBTMPL/ArtifactCleanup`
     Deprecated predecessor of this template.
   :ref:`DEV/ConditionalJobs`
     Why an ``if:`` without a status check function skips the cleanup.


.. _JOBTMPL/CleanupArtifacts/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/CleanupArtifacts/Inputs>`

+------------------------------------------------------------+----------+---------+-------------+
| Parameter Name                                             | Required | Type    | Default     |
+============================================================+==========+=========+=============+
| :ref:`JOBTMPL/CleanupArtifacts/Input/ubuntu_image_version` | no       | string  | ``'26.04'`` |
+------------------------------------------------------------+----------+---------+-------------+
| :ref:`JOBTMPL/CleanupArtifacts/Input/json`                 | no       | string  | ``'{}'``    |
+------------------------------------------------------------+----------+---------+-------------+
| :ref:`JOBTMPL/CleanupArtifacts/Input/condition`            | no       | boolean | ``true``    |
+------------------------------------------------------------+----------+---------+-------------+
| :ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids`    | no       | string  | ``''``      |
+------------------------------------------------------------+----------+---------+-------------+
| :ref:`JOBTMPL/CleanupArtifacts/Input/json2`                | no       | string  | ``'{}'``    |
+------------------------------------------------------------+----------+---------+-------------+
| :ref:`JOBTMPL/CleanupArtifacts/Input/condition2`           | no       | boolean | ``true``    |
+------------------------------------------------------------+----------+---------+-------------+
| :ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids2`   | no       | string  | ``''``      |
+------------------------------------------------------------+----------+---------+-------------+
| :ref:`JOBTMPL/CleanupArtifacts/Input/others`               | no       | string  | ``''``      |
+------------------------------------------------------------+----------+---------+-------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/CleanupArtifacts/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/CleanupArtifacts/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/CleanupArtifacts/Inputs:

Input Parameters
****************

.. _JOBTMPL/CleanupArtifacts/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/CleanupArtifacts/Input/json:

json
====

:Type:            string (JSON)
:Required:        no
:Default Value:   ``'{}'``
:Possible Values: Any valid JSON string containing a JSON object mapping keys to artifact names.
:Description:     Dictionary of artifact names the first set of IDs is resolved against. |br|
                  Usually taken from :ref:`JOBTMPL/Parameters/Output/artifact_names`.


.. _JOBTMPL/CleanupArtifacts/Input/condition:

condition
=========

:Type:            boolean
:Required:        no
:Default Value:   ``true``
:Possible Values: ``true`` / ``false``
:Description:     Guard for the first set of artifacts. |br|
                  ``true`` - delete the artifacts computed from
                  :ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids`. |br|
                  ``false`` - keep them.


.. _JOBTMPL/CleanupArtifacts/Input/artifact-json-ids:

artifact-json-ids
=================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A space or newline separated list of entries - see
                  :ref:`JOBTMPL/CleanupArtifacts/ArtifactIDs`.
:Description:     Keys of the first set of artifacts to be deleted.


.. _JOBTMPL/CleanupArtifacts/Input/json2:

json2
=====

:Type:            string (JSON)
:Required:        no
:Default Value:   ``'{}'``
:Possible Values: Any valid JSON string containing a JSON object mapping keys to artifact names.
:Description:     Dictionary of artifact names the second set of IDs is resolved against. |br|
                  Usually the same dictionary as :ref:`JOBTMPL/CleanupArtifacts/Input/json`; the second set exists for
                  its separate condition, not for a different dictionary.


.. _JOBTMPL/CleanupArtifacts/Input/condition2:

condition2
==========

:Type:            boolean
:Required:        no
:Default Value:   ``true``
:Possible Values: ``true`` / ``false``
:Description:     Guard for the second set of artifacts. |br|
                  ``true`` - delete the artifacts computed from
                  :ref:`JOBTMPL/CleanupArtifacts/Input/artifact-json-ids2`. |br|
                  ``false`` - keep them.


.. _JOBTMPL/CleanupArtifacts/Input/artifact-json-ids2:

artifact-json-ids2
==================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A space or newline separated list of entries - see
                  :ref:`JOBTMPL/CleanupArtifacts/ArtifactIDs`.
:Description:     Keys of the second set of artifacts to be deleted.


.. _JOBTMPL/CleanupArtifacts/Input/others:

others
======

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A newline separated list of artifact names. Glob patterns are supported.
:Description:     Further artifacts to be deleted by literal name, for artifacts that are not part of an artifact-name
                  dictionary.


.. _JOBTMPL/CleanupArtifacts/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/CleanupArtifacts/Outputs:

Outputs
*******

This job template has no output parameters.

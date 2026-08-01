Development
###########

.. todo:: Development - Explain how to write new job templates.


.. _DEV/ConditionalJobs:

Conditional Jobs
****************

Almost every job template offers switches to disable parts of a pipeline: ``apptest``, ``documentation_steps``,
``cleanup``, ... A disabled job is not removed from the pipeline, it is *skipped*, and a skipped job influences all
jobs depending on it. Handling that influence correctly is the single most error-prone part of writing a job template,
therefore the rules are collected here.


.. _DEV/ConditionalJobs/StatusCheckFunctions:

Status Check Functions
======================

GitHub Actions offers four *status check functions*, which can be used in a job's ``if`` expression:

+---------------------+------------------------------------------------------------------------------------------+
| Function            | Result                                                                                   |
+=====================+==========================================================================================+
| ``success()``       | ``true``, if no job the current job depends on failed or was skipped.                    |
+---------------------+------------------------------------------------------------------------------------------+
| ``failure()``       | ``true``, if any job the current job depends on failed.                                  |
+---------------------+------------------------------------------------------------------------------------------+
| ``cancelled()``     | ``true``, if the workflow was cancelled.                                                 |
+---------------------+------------------------------------------------------------------------------------------+
| ``always()``        | ``true``, always - even if the workflow was cancelled.                                   |
+---------------------+------------------------------------------------------------------------------------------+

If a job has an ``if`` expression, but that expression contains **no** status check function at all, GitHub adds an
implicit ``success()``. This is the behavior that surprises most template authors, because such a condition reads like
a pure feature switch, while it also demands that every dependency succeeded.

.. code-block:: yaml

   # This condition is evaluated as:  success() && contains(inputs.documentation_steps, 'pages')
   if: ${{ contains(inputs.documentation_steps, 'pages') }}


.. _DEV/ConditionalJobs/Propagation:

Propagation of Skipped Jobs
===========================

The status check functions are not evaluated on the jobs listed in ``needs``, but on the **transitive dependency
closure** of the job: all jobs reachable from the current job by following ``needs`` edges. Therefore a skipped job
propagates its state to jobs it isn't directly connected to.

An intermediate job does **not** stop that propagation. A job surviving on ``!cancelled()`` runs itself, but the
skipped ancestor remains part of the closure of all its successors:

.. code-block::

   AppTestingParams  ->  AppTesting  ->  PublishTestResults  ->  Documentation  ->  PDFDocumentation
     (skipped by            (skipped)      (if: !cancelled()     (if: !cancelled()   (if: contains(...))
      apptest: false)                       - runs)               - runs)             => skipped!

With ``apptest: false``, ``PDFDocumentation`` was skipped although its own condition was ``true`` and neither of its
two ``needs`` jobs was skipped. Symmetrically, a job outside the closure cannot suppress a job guarded by
``!failure()``.

.. attention::

   A skipped job is not an error, so nothing in the pipeline turns red. The affected jobs are simply missing from the
   run, which makes this class of defect easy to overlook - the pipeline is green, but it did less than it claims.


.. _DEV/ConditionalJobs/Guidelines:

Guidelines
==========

Every job whose ``if`` expression contains a feature switch needs an explicit status check function, otherwise the
implicit ``success()`` links the switch to unrelated jobs:

.. code-block:: yaml

   if: >-
     ${{ !failure() && !cancelled()
      && contains(inputs.documentation_steps, 'pages')
     }}

Which function to choose:

* ``!failure() && !cancelled()`` - the job's own condition decides, a skipped dependency is tolerated, but a failed
  dependency suppresses the job. This is the default for optional jobs (:ref:`JOBTMPL/PublishToGitHubPages`,
  :ref:`JOBTMPL/LaTeXDocumentation`) as well as for release jobs, which must not run if any check failed.
* ``!cancelled()`` - the job runs regardless of the outcome of its dependencies. Use it for jobs collecting or
  cleaning up results (:ref:`JOBTMPL/PublishTestResults`, ``CleanupArtifacts``), because artifacts of a failed run
  still need to be published or deleted.
* ``always()`` - avoid it. It also runs the job when the workflow was cancelled, which delays the cancellation.

.. hint::

   Do not use ``success() || failure()`` as a substitute for ``!cancelled()``. It is ``false`` if a dependency was
   *skipped*, because a skipped dependency is neither a success nor a failure.

Conditions combining a status check function with further terms are written as a folded block scalar, one term per
line, so a condition can be read - and reviewed - without horizontal scrolling:

.. code-block:: yaml

   if: >-
     ${{ !failure() && !cancelled()
      && needs.Prepare.outputs.is_release_commit == 'true'
      && github.event_name != 'schedule'
     }}


.. _DEV/ConditionalJobs/Verification:

Verification
============

A skipped job cannot be detected by looking at a green pipeline, so each combination needs a verification pipeline that
actually exercises it. The templates in :file:`.github/workflows/_Checking_*.yml` cover the relevant combinations:
:file:`_Checking_SimplePackage_Pipeline.yml` runs with application testing enabled, while
:file:`_Checking_NamespacePackage_Pipeline.yml` disables it and requests ``html latex pdf``, so it combines a skipped
job with jobs conditioned on ``documentation_steps``.

When a new switch is added to a job template, add a combination disabling it to one of these pipelines and check the
list of executed jobs of the resulting run, not only its conclusion.

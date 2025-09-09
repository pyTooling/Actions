.. _JOBTMPL/TagReleaseCommit:

TagReleaseCommit
################

The ``TagReleaseCommit`` job template creates a tag at the commit currently used by the pipeline run and then it
triggers a new pipeline run for that tag, a.k.a *tag pipeline* or *release pipeline*.

.. note::

   When the *tag pipeline* is launched, the pipeline is displayed in GitHub Actions with the name in the YAML file. In
   contrast, when a tag is manually added and pushed via Git on command line, the tag name is displayed.

   Currently, no command, API or similar is known to add a tag and trigger a matching pipeline run, where the pipeline
   is named like the used tag. Thus, currently this job template has a slightly different behavior compared to manual
   tagging and pushing a tag to GitHub.

   In addition, GitHub doesn't support *project access token*, thus there is no solution to create a user independent
   token to emulate a manual push operation.

.. topic:: Features

   * Tag the current pipeline's commit.
   * Trigger a new pipeline run for this new tag.

.. topic:: Behavior

   1. Tag the current commit with a tag named like :ref:`JOBTMPL/TagReleaseCommit/Input/version`.
   2. Trigger a pipeline run for the new tag.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-TagReleaseCommit.png
      :width: 350px

.. topic:: Dependencies

   * :gh:`actions/github-script`


.. _JOBTMPL/PrepareJob/Instantiation:

Instantiation
*************

The following instantiation example depicts three jobs within a bigger pipeline. The ``prepare`` job derived from job
template ``PrepareJob`` version ``@r5`` figures out if a pipeline runs for a release merge-commit, for a tag or any
other reason. Its outputs are used to either run a ``TriggerTaggedRelease`` job derived from job template
``TagReleaseCommit`` version ``@r5``, or alternatively run the ``ReleasePage`` job derived from job template
``PublishReleaseNotes`` version ``@r5``.

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     Prepare:
       uses: pyTooling/Actions/.github/workflows/PrepareJob.yml@r5

     # Other pipeline jobs

     TriggerTaggedRelease:
       uses: pyTooling/Actions/.github/workflows/TagReleaseCommit.yml@r5
       needs:
         - Prepare
       if: needs.Prepare.outputs.is_release_commit == 'true' && github.event_name != 'schedule'
       permissions:
         contents: write  # required for create tag
         actions:  write  # required for trigger workflow
       with:
         version:  ${{ needs.Prepare.outputs.version }}
         auto_tag: ${{ needs.Prepare.outputs.is_release_commit }}
       secrets: inherit

     ReleasePage:
       uses: pyTooling/Actions/.github/workflows/PublishReleaseNotes.yml@r5
       needs:
         - Prepare
       if: needs.Prepare.outputs.is_release_tag == 'true'
       permissions:
         contents: write
         actions:  write
       with:
         tag: ${{ needs.Prepare.outputs.version }}
       secrets: inherit


.. _JOBTMPL/TagReleaseCommit/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/TagReleaseCommit/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/TagReleaseCommit/Input/ubuntu_image`                  | no       | string   | ``'ubuntu-24.04'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/TagReleaseCommit/Input/version`                       | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/TagReleaseCommit/Input/auto_tag`                      | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/TagReleaseCommit/Input/workflow`                      | no       | string   | ``'Pipeline.yml'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/TagReleaseCommit/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/TagReleaseCommit/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/TagReleaseCommit/Inputs:

Input Parameters
****************

.. _JOBTMPL/TagReleaseCommit/Input/ubuntu_image:

ubuntu_image
============

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu-24.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Name of the Ubuntu image used to run this job.


.. _JOBTMPL/TagReleaseCommit/Input/version:

version
=======

:Type:            string
:Required:        yes
:Possible Values: Any valid Git tag name.
:Description:     The version string to be used for tagging.


.. _JOBTMPL/TagReleaseCommit/Input/auto_tag:

auto_tag
========

:Type:            string
:Required:        yes
:Possible Values: ``'false'``, ``'true'```
:Description:     If *true*, tag the current commit.


.. _JOBTMPL/TagReleaseCommit/Input/workflow:

workflow
========

:Type:            string
:Required:        no
:Default Value:   ``'Pipeline.yml'``
:Possible Values: Any valid GitHub Action pipeline filename.
:Description:     Github Action pipeline (workflow) to trigger after tag creation.

                  .. note::

                     Compared to manual tagging and pushing a tag, where a pipeline is triggered automatically, here a
                     pipeline must be trigger separately by API. Therefore the pipeline doesn't run with the name of the
                     tag, but with the name specified within the workflow YAML file.


.. _JOBTMPL/TagReleaseCommit/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/TagReleaseCommit/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/TagReleaseCommit/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

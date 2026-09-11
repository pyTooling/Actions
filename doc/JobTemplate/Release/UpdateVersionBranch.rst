.. _JOBTMPL/UpdateVersionBranch:
.. index::
   single: gh; UpdateVersionBranch Template
   single: GitHub Action Reusable Workflow; UpdateVersionBranch Template

UpdateVersionBranch
###################

The ``UpdateVersionBranch`` job template proposes the update of a major-version branch. Consumers of an action or of a
reusable workflow pin a major version (``@v1``, ``@r8``), so every release has to move that branch. This template opens
the pull-request that does it, titled like ``Updating r8 from v8.1.0``, which is reviewed and merged like any other.

It is intended to run in the *tag pipeline*, beside :ref:`JOBTMPL/PublishReleaseNotes`.

.. note::

   A major version that has no branch yet is created **from the previous major**, not from the main branch. A branch
   cut from the main branch is already identical to it, so there would be nothing to open a pull-request about.
   Branching from the previous major keeps the new branch behind the main branch, and the pull-request then carries
   exactly the changes between the last release of the previous major and the new one.

   The highest existing lower major is used, so a jump from ``r3`` to ``r9`` works without an ``r8`` in between.

.. topic:: Features

   * Create the major-version branch, if it doesn't exist yet.
   * Rewrite references to this repository so they name the version branch.
   * Open (or retitle) the pull-request updating the version branch from the main branch.

.. topic:: Behavior

   1. Derive the branch name from :ref:`JOBTMPL/UpdateVersionBranch/Input/prefix` and either
      :ref:`JOBTMPL/UpdateVersionBranch/Input/major` or the major number of
      :ref:`JOBTMPL/UpdateVersionBranch/Input/version`. A major that isn't a number is an error.
   2. Create the branch if it is missing, from the highest existing lower major, or from
      :ref:`JOBTMPL/UpdateVersionBranch/Input/main_branch` when there is none.
   3. Rewrite references to this repository - ``<owner>/<repository>[/<path>]@<ref>`` and the ``branch=`` parameter of
      a workflow-status badge - in the tracked ``*.yml``, ``*.yaml`` and ``*.md`` files. Where a rewrite is needed, it
      becomes a commit on ``<update_branch_prefix><branch>`` and the pull-request is opened from there; where nothing
      needs rewriting, the pull-request is a plain merge of the main branch.
   4. Open the pull-request, or retitle the one still open from the previous release.

   The job does nothing when the version branch is already level with the main branch.

   .. note::

      Only **self**-references are rewritten. A reference to another repository, such as ``actions/checkout@v7``, is a
      separate decision and is left alone, as is ``./``, which resolves to the calling ref by itself.

      Prose *about* a reference is not rewritten either - the scan matches ``<owner>/<repository>@<ref>``, not an
      English sentence mentioning a branch name.

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * GitHub CLI (``gh``), pre-installed on GitHub-hosted runners.

.. _JOBTMPL/UpdateVersionBranch/Instantiation:

Instantiation
*************

The following instantiation example depicts the job beside a ``ReleasePage`` job in the same *tag pipeline*. Both are
gated on ``is_release_tag`` from a ``Prepare`` job derived from job template :ref:`JOBTMPL/PrepareJob`.

.. code-block:: yaml

   jobs:
     Prepare:
       uses: pyTooling/Actions/.github/workflows/PrepareJob.yml@r8

     # Other pipeline jobs

     ReleasePage:
       uses: pyTooling/Actions/.github/workflows/PublishReleaseNotes.yml@r8
       needs:
         - Prepare
       if: needs.Prepare.outputs.is_release_tag == 'true'
       with:
         tag: ${{ needs.Prepare.outputs.version }}
       secrets: inherit

     UpdateVersionBranch:
       uses: pyTooling/Actions/.github/workflows/UpdateVersionBranch.yml@r8
       needs:
         - Prepare
       if: needs.Prepare.outputs.is_release_tag == 'true'
       permissions:
         contents:      write   # required to create a version branch
         pull-requests: write   # required to open the pull-request
       with:
         version: ${{ needs.Prepare.outputs.version }}
         prefix:  'r'


.. _JOBTMPL/UpdateVersionBranch/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/UpdateVersionBranch/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/UpdateVersionBranch/Input/version`                    | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Input/prefix`                     | no       | string   | ``'v'``                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Input/major`                      | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Input/main_branch`                | no       | string   | ``'main'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Input/update_branch_prefix`       | no       | string   | ``'update/'``                                                     |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Input/ubuntu_image`               | no       | string   | ``'ubuntu-26.04'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/UpdateVersionBranch/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/UpdateVersionBranch/Outputs>`

+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Type     | Description                                                       |
+=====================================================================+==========+===================================================================+
| :ref:`JOBTMPL/UpdateVersionBranch/Output/branch`                    | string   | Name of the version branch.                                       |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Output/branch-created`            | string   | ``'true'`` if the branch was created by this run.                 |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Output/head`                      | string   | Branch the pull-request was opened from.                          |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Output/rewritten`                 | string   | ``'true'`` if references had to be rewritten.                     |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/UpdateVersionBranch/Output/pull-request`              | string   | URL of the pull-request, empty if none was needed.                |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+


.. _JOBTMPL/UpdateVersionBranch/Inputs:

Input Parameters
****************

.. _JOBTMPL/UpdateVersionBranch/Input/version:

version
=======

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: A version with a leading major number, optionally prefixed by ``v`` or ``r``, e.g. ``v8.1.0``,
                  ``r8.1.0`` or ``8.1.0``.
:Description:     The released version, as tagged. Its **major** number selects the version branch: ``v1.2.3`` with
                  prefix ``r`` targets branch ``r1``. |br|
                  Usually :ref:`JOBTMPL/PrepareJob`'s ``version`` output parameter.


.. _JOBTMPL/UpdateVersionBranch/Input/prefix:

prefix
======

:Type:            string
:Required:        no
:Default Value:   ``'v'``
:Possible Values: Usually ``'v'`` or ``'r'``.
:Description:     Prefix of the version branch name. It is independent of the version's own prefix, so a repository
                  tagging ``v8.1.0`` while publishing ``r8`` branches sets ``'r'`` here.


.. _JOBTMPL/UpdateVersionBranch/Input/major:

major
=====

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A non-negative integer, or empty.
:Description:     Major version number selecting the version branch. When empty, the major number of
                  :ref:`JOBTMPL/UpdateVersionBranch/Input/version` is used. |br|
                  Set it where the version branch doesn't follow the released version's major at all -
                  :gh:`pyTooling/download-artifact` tags ``v1.10.0`` while publishing a ``v8`` branch, so it passes
                  ``major: '8'``.


.. _JOBTMPL/UpdateVersionBranch/Input/main_branch:

main_branch
===========

:Type:            string
:Required:        no
:Default Value:   ``'main'``
:Possible Values: Any branch name.
:Description:     Branch the version branch is updated from - the branch releases are tagged on.


.. _JOBTMPL/UpdateVersionBranch/Input/update_branch_prefix:

update_branch_prefix
====================

:Type:            string
:Required:        no
:Default Value:   ``'update/'``
:Possible Values: Any branch name prefix.
:Description:     Prefix of the branch carrying the rewritten references. It is used only when a rewrite is needed,
                  and is force-pushed on every release, so nothing should pin it.


.. _JOBTMPL/UpdateVersionBranch/Input/ubuntu_image:

ubuntu_image
============

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu-26.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Name of the Ubuntu image used to run this job.


.. _JOBTMPL/UpdateVersionBranch/Secrets:

Secrets
*******

This job template needs no secrets. It uses the automatic ``GITHUB_TOKEN``, which needs ``contents: write`` and
``pull-requests: write`` granted by the calling job.


.. _JOBTMPL/UpdateVersionBranch/Outputs:

Outputs
*******

.. _JOBTMPL/UpdateVersionBranch/Output/branch:

branch
======

:Type:        string
:Description: Name of the version branch, e.g. ``r8``.


.. _JOBTMPL/UpdateVersionBranch/Output/branch-created:

branch-created
==============

:Type:        string
:Description: ``'true'`` if the version branch didn't exist and was created by this run, ``'false'`` otherwise.


.. _JOBTMPL/UpdateVersionBranch/Output/head:

head
====

:Type:        string
:Description: Branch the pull-request was opened from: the main branch, or the update branch when references were
              rewritten.


.. _JOBTMPL/UpdateVersionBranch/Output/rewritten:

rewritten
=========

:Type:        string
:Description: ``'true'`` if references to this repository had to be rewritten for the version branch.


.. _JOBTMPL/UpdateVersionBranch/Output/pull-request:

pull-request
============

:Type:        string
:Description: URL of the created or updated pull-request. Empty when the version branch was already level with the
              main branch.


.. _JOBTMPL/UpdateVersionBranch/Optimizations:

Optimizations
*************

The reference rewrite is skipped entirely when no tracked file mentions this repository, in which case the
pull-request is a plain merge and no update branch is pushed.

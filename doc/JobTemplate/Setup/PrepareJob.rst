.. _JOBTMPL/PrepareJob:
.. index::
   single: GitHub Action Reusable Workflow; PrepareJob Template

PrepareJob
##########

The ``PrepareJob`` template is a workaround for the limitations of GitHub Actions to handle global variables in GitHub
Actions workflows (see `actions/runner#480 <https://github.com/actions/runner/issues/480>`__) as well as providing basic
string operations (see GitHub Action's `limited set of functions <https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#functions>`__).

The job template generates various output parameters derived from
`${{ github }} context <https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context>`__.

.. topic:: Features

   * Provide branch name or tag name from ``${{ github.ref }}`` variable.
   * Check if pipeline is a branch, tag or pull-request pipeline.
   * Check if a commit is a merge commit.
   * Check if a commit is a release commit.
   * Check if a tag is a nightly tag (rolling release tag).
   * Check if a tag is a release tag.
   * Find associated pull-request (PR) for a merge commit/release commit.
   * Provide a version from tag name or pull-request name.

   .. note::

      Due to GitHub Action's broken type system and missing implicit type conversions in YAML files, *boolean* values need
      to be returned as *string* values otherwise type compatibility and comparison are broken. This also requires all
      inputs to be *string* parameters, otherwise step's, job's or template's output cannot be assigned to a template's
      input.

      **Problems:**

      1. Scripts (Bash, Python, ...) return results as strings. There is no option or operation provided by GitHub Actions
         to convert outputs of ``printf`` to a ``boolean`` in the YAML file.
      2. Unlike job template inputs, outputs have no type information. These are all considered *string* values. Again no
         implicit or explicit type conversion is provided.
      3. While inputs might be defined as ``boolean`` and a matching default can be set as a *boolean* value (e.g.,
         ``false``), a connected variable from ``${{ needs }}`` context will either cause a typing error or a later
         comparison will not work as expected. Either the comparison works with ``inputs.param == false`` for the default
         value, **or** it works with a value from ``${{ needs }}`` context, which is a string ``inputs.param == 'false'``.

.. topic:: Behavior

   1. Checkout repository.
   2. Classify ``${{ github.ref }}`` into branch, tag or pull-request.
   3. Compute output parameters.
   4. Find associated pull-request.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-PrepareJob.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`GitHub command line tool 'gh' <cli/cli>`


.. _JOBTMPL/PrepareJob/Instantiation:

Instantiation
*************

The following instantiation example creates a ``Prepare`` job derived from job template ``PrepareJob`` version ``@r7``.
In a default usecase, no input parameters need to be specified for the job template assuming a main-branch and
release-branch called ``main``, a development-branch called ``dev``, as well as semantic versioning for tags and
pull-request titles.

.. code-block:: yaml

   jobs:
     Prepare:
       uses: pyTooling/Actions/.github/workflows/PrepareJob.yml@r7

     <ReleaseJob>:
       needs:
         - Prepare
       if: needs.Prepare.outputs.is_release_tag == 'true'
       ...
       with:
         version: ${{ needs.Prepare.outputs.version }}

.. seealso::

   :ref:`JOBTMPL/TagReleaseCommit`
     ``PrepareJob`` is usually used to identify if a pipeline's commit is a merge commit created by a pull-request. If
     so, this commit can be tagged automatically to trigger a release pipeline (tag pipeline) for the same commit
     resulting in a full release (PyPI, GitHub Pages, GitHub Release, ...).
   :ref:`JOBTMPL/PublishReleaseNotes`
     ``PrepareJob`` is usually used to identify if a tag pipeline is a release pipeline.


.. _JOBTMPL/PrepareJob/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/PrepareJob/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/PrepareJob/Input/ubuntu_image`                        | no       | string   | ``'ubuntu-24.04'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Input/main_branch`                         | no       | string   | ``'main'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Input/development_branch`                  | no       | string   | ``'dev'``                                                         |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Input/release_branch`                      | no       | string   | ``'main'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Input/nightly_tag_pattern`                 | no       | string   | ``'nightly'``                                                     |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Input/release_tag_pattern`                 | no       | string   | ``'(v|r)?[0-9]+(\.[0-9]+){0,2}(-(dev|alpha|beta|rc)([0-9]*))?'``  |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/PrepareJob/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/PrepareJob/Outputs>`

+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| Result Name                                                         | Type     | Description                                                       |
+=====================================================================+==========+===================================================================+
| :ref:`JOBTMPL/PrepareJob/Output/on_main_branch`                     | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/on_dev_branch`                      | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/on_release_branch`                  | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/is_regular_commit`                  | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/is_merge_commit`                    | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/is_release_commit`                  | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/is_nightly_tag`                     | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/is_release_tag`                     | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/ref_kind`                           | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/branch`                             | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/tag`                                | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/version`                            | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/pr_title`                           | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PrepareJob/Output/pr_number`                          | string   |                                                                   |
+---------------------------------------------------------------------+----------+-------------------------------------------------------------------+


.. _JOBTMPL/PrepareJob/Inputs:

Input Parameters
****************

.. _JOBTMPL/PrepareJob/Input/ubuntu_image:

ubuntu_image
============

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu-24.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Name of the Ubuntu image used to run this job.


.. _JOBTMPL/PrepareJob/Input/main_branch:

main_branch
===========

:Type:            string
:Required:        no
:Default Value:   ``'main'``
:Possible Values: Any valid branch name.
:Description:     Name of the main branch.


.. _JOBTMPL/PrepareJob/Input/development_branch:

development_branch
==================

:Type:            string
:Required:        no
:Default Value:   ``'dev'``
:Possible Values: Any valid branch name.
:Description:     Name of the development branch.


.. _JOBTMPL/PrepareJob/Input/release_branch:

release_branch
==============

:Type:            string
:Required:        no
:Default Value:   ``'main'``
:Possible Values: Any valid branch name.
:Description:     Name of the branch containing releases.


.. _JOBTMPL/PrepareJob/Input/nightly_tag_pattern:

nightly_tag_pattern
===================

:Type:            string
:Required:        no
:Default Value:   ``'nightly'``
:Possible Values: Any valid regular expression. |br|
                  Suggested alternative values: ``latest``, ``rolling``
:Description:     Name of the tag used for rolling releases, a.k.a nightly builds.



.. _JOBTMPL/PrepareJob/Input/release_tag_pattern:

release_tag_pattern
===================

:Type:            string
:Required:        no
:Default Value:   ``'(v|r)?[0-9]+(\.[0-9]+){0,2}(-(dev|alpha|beta|rc)([0-9]*))?'``
:Possible Values: Any valid regular expression.
:Description:     A regular expression describing a pattern for identifying a release tag.

                  The default pattern matches on a `semantic version number <https://semver.org/>`__ separated by dots.
                  It supports up to 3 digit groups. It accepts an optional ``v`` or ``r`` prefix. Optionally, a postfix
                  of ``dev``, ``alpha``, ``beta`` or ``rc`` separated by a hyphen can be appended. If needed, the
                  postfix can have a digit group.

                  **Matching tag names as releases:**

                  * ``v1``, ``r1``
                  * ``1``, ``1.1``, ``1.1.1``
                  * ``v1.2.8-dev``
                  * ``v3.13.5-alpha2``
                  * ``v4.7.22-beta3``
                  * ``v10.2-rc1``

.. _JOBTMPL/PrepareJob/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/PrepareJob/Outputs:

Outputs
*******

.. _JOBTMPL/PrepareJob/Output/on_main_branch:

on_main_branch
==============

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline's commit is on :ref:`main branch <JOBTMPL/PrepareJob/Input/main_branch>`,
                  otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/on_dev_branch:

on_dev_branch
=============

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline's commit is on :ref:`development branch <JOBTMPL/PrepareJob/Input/development_branch>`,
                  otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/on_release_branch:

on_release_branch
=================

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline's commit is on :ref:`release branch <JOBTMPL/PrepareJob/Input/release_branch>`,
                  otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/is_regular_commit:

is_regular_commit
=================

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline's commit is not a :ref:`merge commit <JOBTMPL/PrepareJob/Output/is_merge_commit>`
                  nor :ref:`release commit <JOBTMPL/PrepareJob/Output/is_release_commit>`, otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/is_merge_commit:

is_merge_commit
===============

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline's commit is on :ref:`main branch <JOBTMPL/PrepareJob/Input/main_branch>`
                  or :ref:`development branch <JOBTMPL/PrepareJob/Input/development_branch>` and has more than one
                  parent (merge commit), otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/is_release_commit:

is_release_commit
=================

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline's commit is on :ref:`release branch <JOBTMPL/PrepareJob/Input/release_branch>`
                  and has more than one parent (merge commit), otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/is_nightly_tag:

is_nightly_tag
==============

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline is a tag pipeline for a commit on :ref:`release branch <JOBTMPL/PrepareJob/Input/release_branch>`
                  and the tag's name matches the :ref:`nightly tag pattern <JOBTMPL/PrepareJob/Input/nightly_tag_pattern>`,
                  otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/is_release_tag:

is_release_tag
==============

:Type:            string
:Default Value:   ``'false'``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns ``'true'`` if the pipeline is a tag pipeline for a commit on :ref:`release branch <JOBTMPL/PrepareJob/Input/release_branch>`
                  and the tag's name matches the :ref:`release tag pattern <JOBTMPL/PrepareJob/Input/release_tag_pattern>`,
                  otherwise return ``'false'``.


.. _JOBTMPL/PrepareJob/Output/ref_kind:

ref_kind
========

:Type:            string
:Default Value:   ``'unknown'``
:Possible Values: ``'branch'``, ``'tag'``, ``'pullrequest'``, ``'unknown'``
:Description:     Returns ``'branch'`` if pipeline's commit is on a branch or returns ``'tag'`` if the pipeline runs for
                  a tagged commit, otherwise returns ``'unknown'`` in case of an internal error.

                  If the kind is a branch, the branch name is available in the job's :ref:`JOBTMPL/PrepareJob/Output/branch`
                  result. |br|
                  If the kind is a tag, the tags name is available in the job's :ref:`JOBTMPL/PrepareJob/Output/tag`
                  result. |br|
                  If the kind is a pull-request, the pull request's id is available in the job's :ref:`JOBTMPL/PrepareJob/Output/pr_number`
                  result. |br|
                  Moreover, if the tag matches the :ref:`JOBTMPL/PrepareJob/Input/release_tag_pattern`, the extracted
                  version is available in the job's :ref:`JOBTMPL/PrepareJob/Output/version` result.

                  .. note::

                     GitHub doesn't provide standalone branch or tag information, but provides the variable
                     ``${{ github.ref }}`` specifying the currently active reference (branch, tag, pull, ...). This job
                     template parses the context's variable and derives if a pipeline runs for a commit on a branch or a
                     tagged commit.


.. _JOBTMPL/PrepareJob/Output/branch:

branch
======

:Type:            string
:Default Value:   ``''``
:Possible Values: Any valid branch name.
:Description:     Returns the branch's name the pipeline's commit is associated to, if :ref:`JOBTMPL/PrepareJob/Output/ref_kind`
                  is ``'branch'``, otherwise returns an empty string ``''``.

.. _JOBTMPL/PrepareJob/Output/tag:

tag
===

:Type:            string
:Default Value:   ``''``
:Possible Values: Any valid tag name.
:Description:     Returns the tag's name the pipeline's commit is associated to, if :ref:`JOBTMPL/PrepareJob/Output/ref_kind`
                  is ``'tag'``, otherwise returns an empty string ``''``.


.. _JOBTMPL/PrepareJob/Output/version:

version
=======

:Type:            string
:Default Value:   ``''``
:Possible Values: Any valid version matching :ref:`JOBTMPL/PrepareJob/Input/release_tag_pattern`.
:Description:     In case the pipeline runs for a tag, it returns the tag's name, if the name matches
                  :ref:`JOBTMPL/PrepareJob/Input/release_tag_pattern`, otherwise returns an empty string ``''``. |br|
                  In case the pipeline runs for a branch, then the commit is checked if it's a
                  :ref:`merge commit <JOBTMPL/PrepareJob/Output/is_merge_commit>` and corresponding pull-request (PR) is
                  searched. When a matching PR can be located and it's title matches
                  :ref:`JOBTMPL/PrepareJob/Input/release_tag_pattern`, then this title is returned as a version,
                  otherwise it returns an empty string ``''``.


.. _JOBTMPL/PrepareJob/Output/pr_title:

pr_title
========

:Type:            string
:Default Value:   ``''``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns the associated pull-request's title, if the pipeline's commit is a
                  :ref:`merge commit <JOBTMPL/PrepareJob/Output/is_merge_commit>` and the located pull-request's title
                  for this commit matches :ref:`JOBTMPL/PrepareJob/Input/release_tag_pattern`, otherwise returns an
                  empty string ``''``.


.. _JOBTMPL/PrepareJob/Output/pr_number:

pr_number
=========

:Type:            string
:Default Value:   ``''``
:Possible Values: ``'true'``, ``'false'``
:Description:     Returns the associated pull-request's number, if the pipeline's commit is a
                  :ref:`merge commit <JOBTMPL/PrepareJob/Output/is_merge_commit>` and the located pull-request's title
                  for this commit matches :ref:`JOBTMPL/PrepareJob/Input/release_tag_pattern`, otherwise returns an
                  empty string ``''``.


.. _JOBTMPL/PrepareJob/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

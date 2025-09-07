.. _JOBTMPL/PublishReleaseNotes:

PublishReleaseNotes
###################

This template create a GitHub Release Page and uploads assets to that page.

.. topic:: Features

   * Assembly a release description from various sources:

     * Description file in the repository.
     * Description via job template parameter.
     * Description from associated pull-request.

   * Download artifact and upload selected files as assets to the release page.
   * Add an inventory file in JSON format as asset to each release.
   * Replace placeholders with variable contents.
   * Override the release's title.
   * Create draft releases.
   * Create pre-release release.
   * Create nightly/rolling releases.

.. topic:: Behavior

   1. Checkout repository.
   2. Install dependencies.
   3. Check if it's a full release or nightly release (rolling release).
   4. Delete old release.
   5. Assemble release notes.
   6. Create a new or recreate the release page as draft.
   7. Attach files from artifacts as assets:

      1. Download artifact
      2. Optionally, create compressed archives of that content.
      3. Upload assets to release page.

   8. Remove draft state from new release page.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-PublishReleaseNotes.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * ``gh`` (GitHub command line interface)
   * ``jq`` (JSON processing)
   * apt

     * zstd


.. _JOBTMPL/PublishReleaseNotes/Instantiation:

Instantiation
*************

.. code-block:: yaml

   jobs:
     Prepare:
       uses: pyTooling/Actions/.github/workflows/PrepareJob.yml@r5

     Release:
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

.. seealso::

   :ref:`JOBTMPL/TagReleaseCommit`
     ``TagReleaseCommit`` is


.. _JOBTMPL/PublishReleaseNotes/ReleaseNotes:

Release Notes
*************

Providing a release description (a.k.a release page content) can be achieved from various sources. These sources can
also be compined to a single description. Moreover, the resulting description can contain placeholders which can be
replaced by values provided via parameter :ref:`JOBTMPL/PublishReleaseNotes/Input/replacements`.

Description text from file in the repository
  The job template's parameter :ref:`JOBTMPL/PublishReleaseNotes/Input/description_file` provides a way to read a
  predfined content from a file within the repository. This allows sharing the same text between nightly releases and
  full releases.

  .. note::

     This file can't be computed/modified at pipeline runtime, because a fixed Git commit is checked out for this job
     template run.
Descriptions text from pipeline parameter
  The job template's parameter :ref:`JOBTMPL/PublishReleaseNotes/Input/description` provides a way to either hard code
  a release description in YAML code, or connect a GitHub Action variable ``${{ ... }}`` to that parameter.

  The content is avilable in replament variable ``%%DESCRIPTION%%``.
Description text from associated PullRequest
  If an associated pull-request can be identified for a merge-commit, the pull-requests description can be used as a
  release description.

  The content is avilable in replament variable ``%%PULLREQUEST%%``.
Additional text from :ref:`JOBTMPL/PublishReleaseNotes/Input/description_footer`
  Additionally, a footer text is provided.

  The content is avilable in replament variable ``%%FOOTER%%``.

.. topic:: Order of Processing

   1. If :ref:`JOBTMPL/PublishReleaseNotes/Input/description_file` exists and is not empty, it will serve as the main
      description. If the description contains ``%%...%%`` placeholders, these placeholders will be replaced
      accordingly. If description contains ``%...%`` placeholders, replacement rules provided by
      :ref:`JOBTMPL/PublishReleaseNotes/Input/replacements` will be applied.
   2. If :ref:`JOBTMPL/PublishReleaseNotes/Input/description` is not empty, it will serve as the main description. If
      the description contains ``%%...%%`` placeholders, these placeholders will be replaced accordingly. If description
      contains ``%...%`` placeholders, replacement rules provided by :ref:`JOBTMPL/PublishReleaseNotes/Input/replacements`
      will be applied.
   3. If the associated pull-request exists and is not empty, it's description will serve as the main description. If
      the description contains ``%%...%%`` placeholders, these placeholders will be replaced accordingly. If description
      contains ``%...%`` placeholders, replacement rules provided by :ref:`JOBTMPL/PublishReleaseNotes/Input/replacements`
      will be applied.
   4. Otherwise, an error is raised.

.. topic:: Replacements

   ``%%DESCRIPTION%%``
     Replaces the placeholder with the content from :ref:`JOBTMPL/PublishReleaseNotes/Input/description`.
   ``%%PULLREQUEST%%``, ``%%PULLREQUEST+0%%``, ``%%PULLREQUEST+1%%``, ``%%PULLREQUEST+2%%``, ``%%PULLREQUEST+3%%``
     Replaces the content by the associated pull-requests description text.

     If an indentation level +N (``+1``, ``+2``, ``+3``) is specified, headlines in the pull-request description will be
     moved by N levels down.
   ``%%FOOTER%%``
     Replaces the placeholder with the content from :ref:`JOBTMPL/PublishReleaseNotes/Input/description_footer`.
   ``%%gh_server%%``
     Replaced by the GitHub server URL. |br|
     The value is derived from ``${{ github.server_url }}``.
   ``%%gh_workflow_name%%``
     Replaced by the workflow name. |br|
     The value is derived from ``${{ github.workflow }}``.
   ``%%gh_owner%%``
     Replaced by the repository owner, which is either the name of a GitHub organisation or a GitHub user account. |br|
     The value is derived from ``${{ github.repository_owner }}``.
   ``%%gh_repo%%``
     Replaced by the repository name. |br|
     The value is derived from ``${{ github.repository }}`` by splitting namespace and repository name into the
     ``${repo}`` variable.
   ``%%gh_owner_repo%%``
     Replaced by the repository slug, which is either the name of a GitHub organisation or a GitHub user account
     followed by the repository name concatenated by the slash character. |br|
     The value is derived from ``${{ github.repository }}``.
   ``%%gh_pages%%``
     Replaced by the URL to the associated GitHub Pages webspace. |br|
     The value is formatted as ``https://${{ github.repository_owner }}.github.io/${repo}``.
   ``%%gh_runid%%``
     Replaced by the pipelines ID. |br|
     The value is derived from ``${{ github.run_id }}``
   ``%%gh_actor%%``
     Replaced by the actor (user or bot), who launched the pipeline. |br|
     The value is derived from  ``${{ github.actor }}``.
   ``%%gh_sha%%``
     Replaced by the associated commit's SHA. |br|
     The value is derived from ``${{ github.sha }}``
   ``%%date%%``
     Replaced by the current date. |br|
     The value is formatted as ``$(date '+%Y-%m-%d')``.
   ``%%time%%``
     Replaced by the current date. |br|
     The value is formatted as ``$(date '+%H:%M:%S %Z')``.
   ``%%datetime%%``
     Replaced by the current date. |br|
     The value is formatted as ``$(date '+%Y-%m-%d %H:%M:%S %Z')``.


Examples
========

.. todo::

   * GHDL - uses description_file and description
   * pyTooling - uses pullrequest


.. _JOBTMPL/PublishReleaseNotes/Assets:

Assets
******

.. todo::

   PublishReleaseNotes::Assets Describe artifact to asset transformation

   Format: ``artifact:file:title``

   See also: :ref:`JOBTMPL/PublishReleaseNotes/Input/replacements`


.. _JOBTMPL/PublishReleaseNotes/Inventory:

Inventory
*********

.. todo::

   PublishReleaseNotes::Inventory Describe how inventory files are created.


.. _JOBTMPL/PublishReleaseNotes/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/PublishReleaseNotes/Inputs>`

+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                          | Required | Type     | Default                                                           |
+=========================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/ubuntu_image`                   | no       | string   | ``'ubuntu-24.04'``                                                |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/release_branch`                 | no       | string   | ``'main'``                                                        |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/mode`                           | no       | string   | ``'release'``                                                     |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/tag`                            | yes      | string   | — — — —                                                           |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/title`                          | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/description`                    | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/description_file`               | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/description_footer`             | no       | string   | see parameter details                                             |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/draft`                          | no       | boolean  | ``false``                                                         |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/prerelease`                     | no       | boolean  | ``false``                                                         |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/latest`                         | no       | boolean  | ``false``                                                         |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/replacements`                   | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/assets`                         | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/inventory-json`                 | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/inventory-version`              | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/inventory-categories`           | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/tarball-name`                   | no       | string   | ``'__pyTooling_upload_artifact__.tar'``                           |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/PublishReleaseNotes/Input/can-fail`                       | no       | boolean  | ``false``                                                         |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/PublishReleaseNotes/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/PublishReleaseNotes/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/PublishReleaseNotes/Inputs:

Input Parameters
****************

.. _JOBTMPL/PublishReleaseNotes/Input/ubuntu_image:

ubuntu_image
============

:Type:            string
:Required:        usually no
:Default Value:   ``'ubuntu-24.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Name of the Ubuntu image used to run a job.


.. _JOBTMPL/PublishReleaseNotes/Input/release_branch:

release_branch
==============

:Type:            string
:Required:        no
:Default Value:   ``'main'``
:Possible Values: Any valid Git branch name.
:Description:     Name of the branch containing releases.


.. _JOBTMPL/PublishReleaseNotes/Input/mode:

mode
====

:Type:            string
:Required:        no
:Default Value:   ``'release'``
:Possible Values: ``'release'``, ``'nightly'``
:Description:     The release mode, which is either *nightly* (a.k.a *rolling* release) or *release*.


.. _JOBTMPL/PublishReleaseNotes/Input/tag:

tag
===

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid Git tag name.
:Description:     Name of the release (tag).
:Condition:       It must match an existing tag name in the repository.


.. _JOBTMPL/PublishReleaseNotes/Input/title:

title
=====

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid string suitable for a release title (headline).
:Description:     If this parameter is not empty, the releases title is set, which overrides the default title infered
                  from the associated tag name.


.. _JOBTMPL/PublishReleaseNotes/Input/description:

description
===========

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid (multi-line) Markdown string.
:Description:     The description of the release usually used to render the *release notes*. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/ReleaseNotes` for more details.


.. _JOBTMPL/PublishReleaseNotes/Input/description_file:

description_file
================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Markdown file. |br|
                  Suggested value: :file:`.github/ReleaseDescription.md`.
:Description:     Path to a Markdown file used for the release description. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/ReleaseNotes` for more details.


.. _JOBTMPL/PublishReleaseNotes/Input/description_footer:

description_footer
==================

:Type:            string
:Required:        no
:Default Value:
                  .. code-block::


                     --------
                     Published from [%%gh_workflow_name%%](%%gh_server%%/%%gh_owner_repo%%/actions/runs/%%gh_runid%%) workflow triggered by %%gh_actor%% on %%datetime%%.

                     This automatic release was created by [pyTooling/Actions](http://github.com/pyTooling/Actions)::Release.yml
:Possible Values: Any valid (multi-line) Markdown text.
:Description:     A footer added to the description. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/ReleaseNotes` for more details.


.. _JOBTMPL/PublishReleaseNotes/Input/draft:

draft
=====

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:     If *true*, the release is kept in *draft* state.

                  .. note::

                     GitHub doesn't send e-mail notifications to subscribed users for draft releases.


.. _JOBTMPL/PublishReleaseNotes/Input/prerelease:

prerelease
==========

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:     If *true*, the release is marked as a *pre-release*.


.. _JOBTMPL/PublishReleaseNotes/Input/latest:

latest
======

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:     If *true*, the release is marked as *latest release*.


.. _JOBTMPL/PublishReleaseNotes/Input/replacements:

replacements
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid multi-line string of format ``search=replace`` patterns.
:Description:     The given replacements are used to replace placeholders in :ref:`JOBTMPL/PublishReleaseNotes/Input/description`,
                  :ref:`JOBTMPL/PublishReleaseNotes/Input/description_file`, :ref:`JOBTMPL/PublishReleaseNotes/Input/description_footer`. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/ReleaseNotes` for more details.
:Example:         The following example replaces the placeholder ``%version%`` with the actual version number (infered
                  from tag name by :ref:`JOBTMPL/PrepareJob`.

                  .. code-block:: yaml

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
                         description: |
                           # myPackage %version%

                           This is the latest release of myPackage.
                         replacements: |
                           version=${{ needs.Prepare.outputs.version }}


.. _JOBTMPL/PublishReleaseNotes/Input/assets:

assets
======

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid multi-line string containing artifact to asset transformations. |br|
                  The ``artifact:file:title`` format is explained at :ref:`JOBTMPL/PublishReleaseNotes/Assets`
:Description:     Each line describes which artifacts to download and extract as well as which extracted file to upload
                  as a release asset. The files title can be changed. |br|
                  Replacement rules from parameter :ref:`JOBTMPL/PublishReleaseNotes/Input/replacements` can be used,
                  too. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/Assets` for more details.


.. _JOBTMPL/PublishReleaseNotes/Input/inventory-json:

inventory-json
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid JSON filename. |br|
                  Suggested value: :file:`inventory.json`.
:Description:     If this parameter is not empty, an inventory of all assets will be created and attached as a JSON file
                  to the release. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/Inventory` for more details.


.. _JOBTMPL/PublishReleaseNotes/Input/inventory-version:

inventory-version
=================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid version string.
:Description:     If this parameter is not empty, the version field in the inventory JSON is set to this value. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/Inventory` for more details.

                  .. hint::

                     Especially for *nightly*/*rolling* releases, the used Git tag is a name rather then a version
                     number. Therefore, a version number must be provided thus a nightly release can be identified as
                     ``vX.Y.Z``.


.. _JOBTMPL/PublishReleaseNotes/Input/inventory-categories:

inventory-categories
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A colon separated list of identifiers used as category names in an inventory JSON.
:Description:     For decoding hierarchy levels (categories) in an inventory JSON, the hierarchy of categories can be
                  added to the inventoy JSON. |br|
                  See :ref:`JOBTMPL/PublishReleaseNotes/Inventory` for more details.


.. _JOBTMPL/PublishReleaseNotes/Input/tarball-name:

tarball-name
============

:Type:            string
:Required:        no
:Default Value:   ``'__pyTooling_upload_artifact__.tar'``
:Possible Values: Any valid name for a tarball file.
:Description:
                  .. todo:: PublishReleaseNotes::tarball-name Needs documentation.


.. _JOBTMPL/PublishReleaseNotes/Input/can-fail:

can-fail
========

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:
                  .. todo:: PublishReleaseNotes::can-fail Needs documentation.


.. _JOBTMPL/PublishReleaseNotes/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/PublishReleaseNotes/Outputs:

Outputs
*******

.. _JOBTMPL/PublishReleaseNotes/Output/release-page:

release-page
============

:Type:            string
:Description:     Returns the URL to the release page.
:Example:         ``tbd``


.. _JOBTMPL/PublishReleaseNotes/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

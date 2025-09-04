.. _JOBTMPL/PublishReleaseNotes:

PublishReleaseNotes
###################

This template runs ...

.. topic:: Features

   * tbd

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

     zstd


.. _JOBTMPL/PublishReleaseNotes/Instantiation:

Instantiation
*************

.. code-block:: yaml

   jobs:
     Release:
       uses: pyTooling/Actions/.github/workflows/Release.yml@r5


.. seealso::

   :ref:`JOBTMPL/TagReleaseCommit`
     ``TagReleaseCommit`` is


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
:Required:        no
:Default Value:   ``'ubuntu-24.04'``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/release_branch:

release_branch
==============

:Type:            string
:Required:        no
:Default Value:   ``'main'``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/mode:

mode
====

:Type:            string
:Required:        no
:Default Value:   ``'release'``
:Possible Values: ``'release'``, ``'nightly'``
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/tag:

tag
===

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/title:

title
=====

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/description:

description
===========

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/description_file:

description_file
================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


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
:Possible Values: Any valid text including multi-line text.
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/draft:

draft
=====

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/prerelease:

prerelease
==========

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/latest:

latest
======

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/replacements:

replacements
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/assets:

assets
======

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/inventory-json:

inventory-json
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/inventory-version:

inventory-version
=================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/inventory-categories:

inventory-categories
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/tarball-name:

tarball-name
============

:Type:            string
:Required:        no
:Default Value:   ``'__pyTooling_upload_artifact__.tar'``
:Possible Values: tbd
:Description:     tbd


.. _JOBTMPL/PublishReleaseNotes/Input/can-fail:

can-fail
========

:Type:            :red:`boolean`
:Required:        no
:Default Value:   ``false``
:Possible Values: ``false``, ``true``
:Description:     tbd


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

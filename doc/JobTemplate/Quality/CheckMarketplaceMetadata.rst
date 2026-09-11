.. _JOBTMPL/CheckMarketplaceMetadata:
.. index::
   single: gh; CheckMarketplaceMetadata Template
   single: GitHub Action Reusable Workflow; CheckMarketplaceMetadata Template

CheckMarketplaceMetadata
########################

The ``CheckMarketplaceMetadata`` job template validates an action's metadata file against the rules
`GitHub Marketplace <https://github.com/marketplace?type=actions>`__ applies when an action is listed.

The Marketplace checks this metadata only at publish time, in a web form, and rejects it without much explanation.
This template applies the same rules on every push, so a defect is a red pipeline on the development branch rather
than a rejection months later.

.. note::

   Publishing itself is **not** automated, because there is no API for it: an action is listed by ticking *Publish
   this Action to the GitHub Marketplace* while drafting or editing its release.

   A tag carries exactly one release, and the Marketplace listing is a property of that release rather than a second
   one - so an already-published release is **edited**, not re-created. Drafting a new release for a tag that has one
   fails with *"Duplicate tag name - This tag already has release notes."*

.. topic:: Features

   * Check that the action metadata file exists at the repository root.
   * Check the action's name, description length, branding icon and branding colour.
   * Check that the repository is public.

.. topic:: Behavior

   1. Check that :ref:`JOBTMPL/CheckMarketplaceMetadata/Input/action_file` exists. If it doesn't, the job fails
      immediately - there is nothing else to check.
   2. Read ``name``, ``description`` and ``branding`` with a YAML parser, so a folded or quoted value is measured as
      the Marketplace measures it.
   3. Report every violated rule, then fail if any was found:

      * ``name`` is missing,
      * ``description`` is missing, or is not shorter than :ref:`JOBTMPL/CheckMarketplaceMetadata/Input/description_limit`,
      * ``branding.icon`` is missing or isn't shaped like a Feather icon name,
      * ``branding.color`` is missing or isn't one of ``white``, ``yellow``, ``blue``, ``green``, ``orange``, ``red``,
        ``purple`` or ``gray-dark``,
      * the repository is private.

   .. note::

      Two rules cannot be checked here and are called out in the log instead of being implied:

      * the action's **name has to be unique** across the Marketplace, which no offline check can establish; and
      * ``branding.icon`` is checked for *shape*, not for membership in the accepted subset of
        `Feather <https://feathericons.com>`__ icons - that set is long and changes, so hard-coding it would go stale
        silently.

.. topic:: Dependencies

   * :gh:`actions/checkout`

.. _JOBTMPL/CheckMarketplaceMetadata/Instantiation:

Instantiation
*************

The job needs no parameters when the metadata file is the conventional ``action.yml`` at the repository root. Making
the release jobs depend on it keeps a release from being tagged with metadata the Marketplace would reject.

.. code-block:: yaml

   jobs:
     Marketplace:
       uses: pyTooling/Actions/.github/workflows/CheckMarketplaceMetadata.yml@r8

     # Other pipeline jobs

     TriggerTaggedRelease:
       uses: pyTooling/Actions/.github/workflows/TagReleaseCommit.yml@r8
       needs:
         - Prepare
         - Marketplace
       if: needs.Prepare.outputs.is_release_commit == 'true'
       permissions:
         contents: write
         actions:  write
       with:
         version:  ${{ needs.Prepare.outputs.version }}
         auto_tag: ${{ needs.Prepare.outputs.is_release_commit }}
       secrets: inherit


.. _JOBTMPL/CheckMarketplaceMetadata/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/CheckMarketplaceMetadata/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/CheckMarketplaceMetadata/Input/action_file`           | no       | string   | ``'action.yml'``                                                  |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/CheckMarketplaceMetadata/Input/description_limit`     | no       | number   | ``125``                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/CheckMarketplaceMetadata/Input/ubuntu_image`          | no       | string   | ``'ubuntu-26.04'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/CheckMarketplaceMetadata/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/CheckMarketplaceMetadata/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/CheckMarketplaceMetadata/Inputs:

Input Parameters
****************

.. _JOBTMPL/CheckMarketplaceMetadata/Input/action_file:

action_file
===========

:Type:            string
:Required:        no
:Default Value:   ``'action.yml'``
:Possible Values: ``'action.yml'`` or ``'action.yaml'``.
:Description:     Action metadata file. GitHub Marketplace requires it at the repository root, so a path pointing
                  elsewhere is reported as a violated rule rather than checked.


.. _JOBTMPL/CheckMarketplaceMetadata/Input/description_limit:

description_limit
=================

:Type:            number
:Required:        no
:Default Value:   ``125``
:Possible Values: A positive number.
:Description:     Maximum length of the action's description, **exclusive**. The Marketplace form rejects a longer
                  description with *"Description must be less than 125 characters."*, so a description of exactly
                  this length is already too long.


.. _JOBTMPL/CheckMarketplaceMetadata/Input/ubuntu_image:

ubuntu_image
============

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu-26.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Name of the Ubuntu image used to run this job.


.. _JOBTMPL/CheckMarketplaceMetadata/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/CheckMarketplaceMetadata/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/CheckMarketplaceMetadata/Optimizations:

Optimizations
*************

Every rule is evaluated before the job fails, so one run reports all violations instead of one per pipeline run.

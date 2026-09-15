.. _JOBTMPL/CheckReleaseVersion:
.. index::
   single: PyPI; CheckReleaseVersion Template
   single: GitHub Action Reusable Workflow; CheckReleaseVersion Template

CheckReleaseVersion
###################

The ``CheckReleaseVersion`` job template checks that a version, which is about to be released, isn't released yet in
a package registry. A registry refuses a second upload of the same version, but only at the very end of a release -
after the tag was created and the release page was published and announced.

.. topic:: Features

   * Check that :term:`PyPI` has no release of a version yet.

.. topic:: Behavior

   1. If :ref:`JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate` is ``'true'``, ask PyPI's JSON API for release
      :ref:`JOBTMPL/CheckReleaseVersion/Input/version` of package :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_package`. |br|
      PyPI normalizes the package name (``pyEDAA.Reports`` equals ``pyedaa-reports``) and the version (``v1.2.0`` and
      ``1.2`` equal ``1.2.0``). A leading ``r``, which PyPI doesn't know, is removed first.

   The job fails, if the release exists or if PyPI can't be queried. A yanked release counts as existing, because PyPI
   doesn't accept its version again. A deleted release isn't detected, although PyPI refuses its file names, too.

.. topic:: Dependencies

   * curl

.. _JOBTMPL/CheckReleaseVersion/Instantiation:

Instantiation
*************

The following instantiation example checks a release commit's version before ``TriggerTaggedRelease`` tags it. The
``Prepare`` job derived from job template ``PrepareJob`` version ``@r8`` provides the version from the pull-request's
title, the ``UnitTestingParams`` job derived from ``Parameters`` provides the package's name.

.. code-block:: yaml

   jobs:
     Prepare:
       uses: pyTooling/Actions/.github/workflows/PrepareJob.yml@r8

     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r8
       with:
         package_name: myPackage

     ReleaseCheck:
       uses: pyTooling/Actions/.github/workflows/CheckReleaseVersion.yml@r8
       needs:
         - Prepare
         - UnitTestingParams
       if: needs.Prepare.outputs.is_release_commit == 'true'
       with:
         version:              ${{ needs.Prepare.outputs.version }}
         check_pypi_duplicate: 'true'
         pypi_package:         ${{ needs.UnitTestingParams.outputs.package_fullname }}

     # Other pipeline jobs

     TriggerTaggedRelease:
       uses: pyTooling/Actions/.github/workflows/TagReleaseCommit.yml@r8
       needs:
         - Prepare
         - ReleaseCheck
       if: needs.Prepare.outputs.is_release_commit == 'true' && needs.ReleaseCheck.result == 'success'
       permissions:
         contents: write  # required for create tag
         actions:  write  # required for trigger workflow
       with:
         version:  ${{ needs.Prepare.outputs.version }}
         auto_tag: ${{ needs.Prepare.outputs.is_release_commit }}
       secrets: inherit

.. seealso::

   :ref:`JOBTMPL/TagReleaseCommit`
     Refuses to tag, if the tag or a release page already exists.


.. _JOBTMPL/CheckReleaseVersion/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/CheckReleaseVersion/Inputs>`

+----------------------------------------------------------------+----------+--------+--------------------+
| Parameter Name                                                 | Required | Type   | Default            |
+================================================================+==========+========+====================+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/ubuntu_image`          | no       | string | ``'ubuntu-26.04'`` |
+----------------------------------------------------------------+----------+--------+--------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/version`               | yes      | string | — — — —            |
+----------------------------------------------------------------+----------+--------+--------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate`  | no       | string | ``'false'``        |
+----------------------------------------------------------------+----------+--------+--------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_package`          | no       | string | ``''``             |
+----------------------------------------------------------------+----------+--------+--------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/CheckReleaseVersion/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/CheckReleaseVersion/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/CheckReleaseVersion/Inputs:

Input Parameters
****************

.. _JOBTMPL/CheckReleaseVersion/Input/ubuntu_image:

ubuntu_image
============

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu-26.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Name of the Ubuntu image used to run this job.


.. _JOBTMPL/CheckReleaseVersion/Input/version:

version
=======

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: A version as tagged, e.g. ``'v1.2.3'``.
:Description:     The version, which is about to be released.


.. _JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate:

check_pypi_duplicate
====================

:Type:            string
:Required:        no
:Default Value:   ``'false'``
:Possible Values: ``'true'`` / ``'false'``
:Description:     Check that :term:`PyPI` has no release of :ref:`JOBTMPL/CheckReleaseVersion/Input/version` yet. |br|
                  ``'true'`` - fail, if PyPI has this release of :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_package`. |br|
                  ``'false'`` - don't query PyPI.


.. _JOBTMPL/CheckReleaseVersion/Input/pypi_package:

pypi_package
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any package name on :term:`PyPI`.
:Description:     Name of the package on PyPI. Required, if :ref:`JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate` is ``'true'``.


.. _JOBTMPL/CheckReleaseVersion/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/CheckReleaseVersion/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/CheckReleaseVersion/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

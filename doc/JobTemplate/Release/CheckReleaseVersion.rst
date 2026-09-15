.. _JOBTMPL/CheckReleaseVersion:
.. index::
   single: PyPI; CheckReleaseVersion Template
   single: GitHub Action Reusable Workflow; CheckReleaseVersion Template

CheckReleaseVersion
###################

The ``CheckReleaseVersion`` job template checks a version, which is about to be released: it has to match the version
in the Python code, and it mustn't be released yet in a package registry. A registry refuses a second upload of the
same version, but only at the very end of a release - after the tag was created and the release page was published
and announced.

.. topic:: Features

   * Check that the version to be released matches the ``__version__`` variable in the Python code.
   * Check that a package registry offering the PyPI JSON API - by default :term:`PyPI` - has no release of this version
     yet.

.. topic:: Behavior

   1. Job ``VersionCheck``: compare :ref:`JOBTMPL/CheckReleaseVersion/Input/version` with :ref:`JOBTMPL/CheckReleaseVersion/Input/package_version`, read from
      :ref:`JOBTMPL/CheckReleaseVersion/Input/package_version_file`. Both are parsed as ``pyTooling.Versioning.PythonVersion``, so a ``v`` prefix is
      ignored and ``v1.2.0-rc1`` equals ``1.2.0rc1``. |br|
      The job fails, if the versions differ, if a version can't be parsed, or if there is no version file or no
      ``__version__``.
   2. Job ``RegistryCheck``, if :ref:`JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate` is ``'true'``: ask the JSON API of :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_url`
      for release :ref:`JOBTMPL/CheckReleaseVersion/Input/version` of package :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_package`. |br|
      PyPI normalizes the package name (``pyEDAA.Reports`` equals ``pyedaa-reports``) and the version (``v1.2.0`` and
      ``1.2`` equal ``1.2.0``). The job fails, if the release exists or if the registry can't be queried. A yanked
      release counts as existing, because PyPI doesn't accept its version again. A deleted release isn't detected,
      although PyPI refuses its file names, too.

.. topic:: Dependencies

   * :gh:`actions/setup-python`
   * pyTooling, installed from PyPI
   * curl

.. _JOBTMPL/CheckReleaseVersion/Instantiation:

Instantiation
*************

The following instantiation example checks a version before ``TriggerTaggedRelease`` tags it. The ``Prepare`` job
derived from job template ``PrepareJob`` version ``@r8`` provides the version from the pull-request's title or the tag,
the ``UnitTestingParams`` job derived from ``Parameters`` provides the package's name and the version in its code.
PyPI is only asked on a release commit.

.. code-block:: yaml

   jobs:
     Prepare:
       uses: pyTooling/Actions/.github/workflows/PrepareJob.yml@r8

     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r8
       with:
         package_name: myPackage

     VersionCheck:
       uses: pyTooling/Actions/.github/workflows/CheckReleaseVersion.yml@r8
       needs:
         - Prepare
         - UnitTestingParams
       if: needs.Prepare.outputs.version != ''
       with:
         version:              ${{ needs.Prepare.outputs.version }}
         package_version:      ${{ needs.UnitTestingParams.outputs.package_version }}
         package_version_file: ${{ needs.UnitTestingParams.outputs.package_version_file }}
         check_pypi_duplicate: ${{ needs.Prepare.outputs.is_release_commit }}
         pypi_package:         ${{ needs.UnitTestingParams.outputs.package_fullname }}

     # Other pipeline jobs

     TriggerTaggedRelease:
       uses: pyTooling/Actions/.github/workflows/TagReleaseCommit.yml@r8
       needs:
         - Prepare
         - VersionCheck
       if: needs.Prepare.outputs.is_release_commit == 'true' && needs.VersionCheck.result == 'success'
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

+---------------------------------------------------------------+----------+--------+------------------------+
| Parameter Name                                                | Required | Type   | Default                |
+===============================================================+==========+========+========================+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/ubuntu_image`         | no       | string | ``'ubuntu-26.04'``     |
+---------------------------------------------------------------+----------+--------+------------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/python_version`       | no       | string | ``'3.14'``             |
+---------------------------------------------------------------+----------+--------+------------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/version`              | yes      | string | — — — —                |
+---------------------------------------------------------------+----------+--------+------------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/package_version`      | no       | string | ``''``                 |
+---------------------------------------------------------------+----------+--------+------------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/package_version_file` | no       | string | ``''``                 |
+---------------------------------------------------------------+----------+--------+------------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate` | no       | string | ``'false'``            |
+---------------------------------------------------------------+----------+--------+------------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_url`             | no       | string | ``'https://pypi.org'`` |
+---------------------------------------------------------------+----------+--------+------------------------+
| :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_package`         | no       | string | ``''``                 |
+---------------------------------------------------------------+----------+--------+------------------------+

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
:Description:     Name of the Ubuntu image used to run the jobs.


.. _JOBTMPL/CheckReleaseVersion/Input/python_version:

python_version
==============

:Type:            string
:Required:        no
:Default Value:   ``'3.14'``
:Possible Values: Any Python version provided by :gh:`actions/setup-python`.
:Description:     Python version used to compare the versions.


.. _JOBTMPL/CheckReleaseVersion/Input/version:

version
=======

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: A version as tagged, e.g. ``'v1.2.3'``.
:Description:     The version, which is about to be released.


.. _JOBTMPL/CheckReleaseVersion/Input/package_version:

package_version
===============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A version as written in Python code, e.g. ``'1.2.3'``.
:Description:     The value of ``__version__`` in :ref:`JOBTMPL/CheckReleaseVersion/Input/package_version_file`, as
                  :ref:`JOBTMPL/Parameters/Output/package_version` provides it. |br|
                  An empty string fails the check.


.. _JOBTMPL/CheckReleaseVersion/Input/package_version_file:

package_version_file
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Path to a Python module.
:Description:     The module carrying ``__version__``, as :ref:`JOBTMPL/Parameters/Output/package_version_file` provides
                  it. It is named in error messages. |br|
                  An empty string - no version file was found - fails the check.


.. _JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate:

check_pypi_duplicate
====================

:Type:            string
:Required:        no
:Default Value:   ``'false'``
:Possible Values: ``'true'`` / ``'false'``
:Description:     Check that :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_url` has no release of :ref:`JOBTMPL/CheckReleaseVersion/Input/version` yet. |br|
                  ``'true'`` - fail, if the registry has this release of :ref:`JOBTMPL/CheckReleaseVersion/Input/pypi_package`. |br|
                  ``'false'`` - don't query the registry.


.. _JOBTMPL/CheckReleaseVersion/Input/pypi_url:

pypi_url
========

:Type:            string
:Required:        no
:Default Value:   ``'https://pypi.org'``
:Possible Values: Base URL of a package registry offering the PyPI JSON API (``<pypi_url>/pypi/<package>/<version>/json``),
                  e.g. ``'https://test.pypi.org'``.
:Description:     The package registry asked, if :ref:`JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate` is ``'true'``.


.. _JOBTMPL/CheckReleaseVersion/Input/pypi_package:

pypi_package
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any package name in the package registry.
:Description:     Name of the package in the package registry. Required, if :ref:`JOBTMPL/CheckReleaseVersion/Input/check_pypi_duplicate` is ``'true'``.


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

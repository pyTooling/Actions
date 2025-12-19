.. _JOBTMPL/InstallPackage:
.. index::
   single: pip; InstallPackage Template
   single: GitHub Action Reusable Workflow; InstallPackage Template

InstallPackage (beta)
#####################

The ``InstallPackage`` job template takes a generated Python package and installs it on the target platform. Afterwards
the installation is verified. This aims for packaging and dependency mistakes in the package.

.. topic:: Features

   * Install generated Python package on the target platform.
   * Verify the installed package's version.

.. topic:: Behavior

   * Download Python package as artifact.
   * Prepare the Python environment.
   * Install the Python package using :term:`pip`.
   * Read out and verify the package version.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-InstallPackage.png
      :width: 500px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`msys2/setup-msys2`
   * :gh:`actions/setup-python`
   * pip

     * :pypi:`pip`
     * :pypi:`wheel`


.. _JOBTMPL/InstallPackage/Instantiation:

Instantiation
*************

The following instantiation example creates a ``Install`` job derived from job template ``InstallPackage`` version
`@r7`. It installs the Python package on various platforms using a precomputed job-matrix created by job
``InstallParams``. This job uses the same ``Parameters`` job template as job ``UnitTestingParams``, which was used to
define parameters for the packaging job ``Package``.

.. code-block:: yaml

   jobs:
     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r7
       with:
         package_name: myPackage

     InstallParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r7
       with:
         package_name:        myPackage
         python_version_list: ''

     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r7
       needs:
         - UnitTestingParams
       with:
         artifact: ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).package_all }}

     Install:
       uses: pyTooling/Actions/.github/workflows/InstallPackage.yml@r7
       needs:
         - UnitTestingParams
         - InstallParams
         - Package
       with:
         jobs:         ${{ needs.InstallParams.outputs.python_jobs }}
         wheel:        ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).package_all }}
         package_name: ${{ needs.UnitTestingParams.outputs.package_fullname }}


.. _JOBTMPL/InstallPackage/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/InstallPackage/Inputs>`

+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| Parameter Name                                                          | Required | Type     | Default                                                                                                                           |
+=========================================================================+==========+==========+===================================================================================================================================+
| :ref:`JOBTMPL/InstallPackage/Input/jobs`                                | yes      | string   | — — — —                                                                                                                           |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/InstallPackage/Input/wheel`                               | yes      | string   | — — — —                                                                                                                           |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/InstallPackage/Input/package_name`                        | yes      | string   | — — — —                                                                                                                           |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/InstallPackage/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/InstallPackage/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/InstallPackage/Inputs:

Input Parameters
****************

.. _JOBTMPL/InstallPackage/Input/jobs:

jobs
====

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: A JSON string with an array of dictionaries with the following key-value pairs:

                  :sysicon: icon to display
                  :system:  name of the system
                  :runs-on: virtual machine image and base operating system
                  :runtime: name of the runtime environment if not running natively on the VM image
                  :shell:   name of the shell
                  :pyicon:  icon for CPython or pypy
                  :python:  Python version
                  :envname: full name of the selected environment
:Description:     A JSON encoded job matrix to run multiple Python job variations.


.. _JOBTMPL/InstallPackage/Input/wheel:

wheel
=====

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid artifact name.
:Description:     The artifact containing the packaged Python code as wheel.


.. _JOBTMPL/InstallPackage/Input/package_name:

package_name
============

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid Python package, subpackage or module name.
:Description:     The package or module containing the version information as a string in ``__version__``.


.. _JOBTMPL/InstallPackage/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/InstallPackage/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/InstallPackage/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).
